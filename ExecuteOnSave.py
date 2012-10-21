import sublime
import sublime_plugin
import re


class ExecuteOnSave(sublime_plugin.EventListener):
    def on_post_save(self, view):

        global_settings = sublime.load_settings(__name__ + '.sublime-settings')
        should_build = view.settings().get('build_on_save', global_settings.get('build_on_save', False))
        filter_execute = view.settings().get('filter_execute', global_settings.get('filter_execute', []))

        if not should_build:
            return

        for filter, execute in filter_execute:
            if re.search(filter, view.file_name()):
                view.window().run_command("exec", {"cmd": execute})
