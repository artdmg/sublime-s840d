# -*- encoding: utf-8 -*-
import locale

import sublime
import sublime_plugin

from .. import doc
from .. import lib
from . import codeintel

SCOPE_GCODE = 'source.s840d_gcode - comment - string - support.variable.nck'


class S840dNckViewEvents(sublime_plugin.ViewEventListener):

    @classmethod
    def is_applicable(cls, settings):
        """Enable the listener for G-Code syntax only!"""
        syntax = settings.get('syntax') or ''
        return any(s in syntax for s in (
            's840d_arc', 's840d_def', 's840d_mpf', 's840d_spf', 's840d_tea'))

    @classmethod
    def applies_to_primary_view_only(cls):
        return False

    def on_selection_modified(self):
        """Handle selection changed events."""
        self._expand_selection_on_placeholders()

    def _expand_selection_on_placeholders(self):
        """Select whole placeholder if cursor is on it.

        Placeholders are added by auto-comletions and are intended to be
        replaced completely by valid statements. Therefore they must not be
        edited as normal words but are to be replaced by the next user input.
        """
        PLACEHOLDER_SCOPE = 'comment.block.placeholder'
        selections = self.view.sel()
        for sel in selections:
            point = sel.a
            # continue if cursor is not on a place holder
            if not self.view.match_selector(point, PLACEHOLDER_SCOPE):
                continue
            char = self.view.substr(point)
            # ignore if cursor is on the beginning to make navigation between
            # several placeholders work properly
            if char in '<[':
                continue
            if char in '>]':
                point -= 1
            elif self.view.substr(point - 1) in '<[':
                point += 1
            # expand selection to whole placeholder (without punctuation)
            region = self.view.expand_by_class(
                point, sublime.CLASS_WORD_START | sublime.CLASS_WORD_END, '[]<>')
            # expand region to punctuation and place cursor to beginning
            region.a, region.b = region.b + 1, region.a - 1
            selections.clear()
            selections.add(region)
            break

    def on_query_completions(self, prefix, locations):
        """Provide a list of dynamically created completions."""
        # don't offer anything for multiple cursors
        if len(locations) > 1:
            return ([], sublime.INHIBIT_WORD_COMPLETIONS)
        # start determines which completion to offer
        start = locations[0] - len(prefix)
        # we need to be at least in s840d scope
        if not self.view.match_selector(start, SCOPE_GCODE):
            return None
        # create a list of symbol completions
        completions = list(
            codeintel.symbols.completions(self.view, prefix, start))
        return (completions, sublime.INHIBIT_WORD_COMPLETIONS)

    def on_hover(self, point, hover_zone):
        """Handle the hover event and show tooltip if needed."""
        if hover_zone != sublime.HOVER_TEXT:
            return
        word = self.view.substr(self.view.word(point))
        content = self._tooltip_content(point, word)
        if not content:
            return
        window_width = min(1000, int(self.view.viewport_extent()[0]) - 64)
        self.view.show_popup(
            content=lib.html.POPUP_TEMPLATE.format(content),
            location=point,
            max_width=window_width,
            flags=sublime.HIDE_ON_MOUSE_MOVE_AWAY,
            on_navigate=self.on_navigate)

    def _tooltip_content(self, point, word):

        try:
            # load current OS display language (e.g.: de_DE)
            lang = locale.getdefaultlocale()[0][:2].lower()
            # get description for machine data or nck variable
            if self.view.match_selector(point, 'support.variable.nck'):
                content = doc.database.tooltip(self.view, word, lang)
            elif self.view.match_selector(point, 'variable | entity.name.tag'):
                content = codeintel.symbols.tooltip(self.view, point, word)
            else:
                content = None
        except Exception as error:
            print(error)
            content = None
        return content

    def on_navigate(self, href):
        """Handle link clicks within the tooltip.

        Arguments:
            href (string):
                The url of the clicked link.
        """
        # open file (open:<file_path>:<row>:<col>)
        if href.startswith('open:'):
            window = self.view.window() or sublime.active_window()
            window.open_file(
                href[5:], group=window.active_group(),
                flags=sublime.TRANSIENT | sublime.ENCODED_POSITION |
                sublime.FORCE_GROUP)

        # scroll action (scroll:<point>)
        elif href.startswith('scroll:'):
            lib.view.goto_point(self.view, int(href[7:]))
