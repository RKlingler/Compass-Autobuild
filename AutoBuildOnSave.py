from os.path import splitext, basename
import sublime_plugin

class AutoBuildOnSave(sublime_plugin.EventListener):
	def on_post_save(self, view):
		fileTypesToBuild = [".sass", ".scss"]
		filePath = view.file_name()
		fileName, fileType = splitext(basename(filePath))

		if fileType in fileTypesToBuild:
			view.window().run_command("build")
		else:
			return []
