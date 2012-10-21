ExecuteOnSave Sublime Text 2 Plugin
===================================

This simple plugin executes a command or multiple commands when a specific file is saved.

(Inspired by https://github.com/alexnj/SublimeOnSaveBuild)

Installation
------------

**Without Git:** Download the latest source from [GitHub](https://github.com/luwes/ExecuteOnSave) and copy the ExecuteOnSave folder to your Sublime Text 2 "Packages" directory.

**With Git:** Clone the repository in your Sublime Text 2 "Packages" directory:

    git clone git://github.com/alexnj/ExecuteOnSave.git


The "Packages" directory is located at:

* OS X:

        ~/Library/Application Support/Sublime Text 2/Packages/

* Linux:

        ~/.config/sublime-text-2/Packages/

* Windows:

        %APPDATA%/Sublime Text 2/Packages/


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

In this case javascript files that are saved trigger an execution of the ..repo/build.sh file and actionscript files that are saved trigger an execution of the ..repo/flash/build.sh.

