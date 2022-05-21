# LeanCloud Flow Control monitoring scheduled Tasks(Github Action)
[简体中文](https://github.com/ReverseSacle/Auto_Wake_LeanCloud/blob/main/README.md) | [English](https://github.com/ReverseSacle/Auto_Wake_LeanCloud/blob/main/README_EN.md)

# Requirements
+ You must have a Token with name  `GITHUB_TOKEN`，which have the right of `repo`，`admin:repo_hook` and `workflow`

# Quickly Start
+ Fork this repository and Find the `secrets` in the settings of repository
+ Then,Get in the `Actions secrets`,Add a secret with name `SITE` which content is the Production Environment Address of LeanCloud(just like https://xxxxx.avosapps.us/)
+ The last,See whether normal in the Actions
+ In addtion,if you want to switch on `Auto Clean Commit` by youself,you could click `Run workflow` in the corresponding action task of Actions

# Detail
## Ⅰ.Get_SiteUrl.py
+ For getting your Production Environment Address of LeanCloud

## Ⅱ.AutoClean.yml
+ Actions File, For cleaning the commit created in the process of Action
+ The Default of Schedule Time is the stander of UTC, `01:00` in Tusday and wednesday(You could modify this by changing the value of `-cron` in AutoClean.yml file)
+ The main subjects of cleaning are those commit which have been existed for 4 day(You could modify this by changing the `value of days_to_expiration`)
+ The main page of cleaning is 12(You could modify this by changing the value of `pages`)
+ Supporting wake by youself

## Ⅲ.AutoWake.yml
+ Actions File,For wake Leancloud engine caused by flow control
+ The Defaut of Schedule Time is the stander of UTC, every day `0:00` to `15:00` (You could modify this by changing the value of `-cron` in AutoWake.yml file )
+ Supporting wake by youself


# Reference
+ [Ching Chow](https://github.com/chingc) put forward the method of cleaning in the question of [`Delete old workflow results`](https://github.community/t/delete-old-workflow-results/16152/2)
+ [wq-h](https://github.com/wq-h) put forward the wake method of Leancloud in the repositroy of [`WakeLeanCloud`](https://github.com/wq-h/WakeLeanCloud)
