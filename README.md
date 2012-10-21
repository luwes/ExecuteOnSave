ExecuteOnSave Sublime Text 2 Plugin
===================================

This simple plugin executes a command or multiple commands when a specific file is saved.

(Inspired by https://github.com/alexnj/SublimeOnSaveBuild)

Configuration
-------------

There are a number of configuration options available to customize the behavior of ExecuteOnSave. For the latest information on what options are available, select the menu item `Preferences->Package Settings->ExecuteOnSave->Settings - Default`.

Do NOT edit the default ExecuteOnSave settings. Your changes will be lost when ExecuteOnSave is updated. ALWAYS edit the project ExecuteOnSave settings by selecting `Project->Edit Project`. 

* **build_on_save**
Set to `1` to trigger a build on save. By default, this is set to `0`.

* **filter_execute**
Is an array that holds one array or multiple arrays with a length of 2. The first element is a regular expression that specifies on which files that are saved the command should be executed. The second element is the command that should be executed. Okay this sounds way too complicated, an example should clear this up.

Example project file:

	{
		"folders":
		[
			{
				"path": "/Users/username/Sites/projects/flow2/repo"
			}
		],
		"settings":
		{
			"filter_execute":[
				["\\.js$", "/Users/username/Sites/projects/flow2/repo/build.sh"],
				["\\.as$", "/Users/username/Sites/projects/flow2/repo/flash/build.sh"]
			],
			"build_on_save": 1
		}
	}
