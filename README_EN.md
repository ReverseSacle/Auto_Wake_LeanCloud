# LeanCloud Flow Control monitoring scheduled tasks(Github Action)
[简体中文](https://github.com/ReverseSacle/Auto_Wake_LeanCloud/blob/main/README.md) | [English](https://github.com/ReverseSacle/Auto_Wake_LeanCloud/blob/main/README_EN.md)

# Requirements
+ You must have a Token with name  `GITHUB_TOKEN`，which have the right of `repo`，`admin:repo_hook` and `workflow`

# Quickly Start
+ Fork this repository and Find the `secrets` in the settings of repository
+ Then,get in the `Actions secrets`,add a secret with name `SITE` which content is the Production Environment Address of LeanCloud
+ The last,see whether normal in the Actions,and redeploy in the engine of LeanCloud
+ In addtion,if you want to switch on `Auto Clean Commit` by yourself,you could click `Run workflow` in the corresponding action task of Actions

# Detail
## Ⅰ.Get_SiteUrl.py
+ For getting your Production Environment Address of LeanCloud

## Ⅱ.AutoClean.yml
+ Actions File, for cleaning the commit created in the process of Action
+ The default of schedule time is the stander of UTC, `01:00` in Tusday and wednesday(You could modify this by changing the value of `-cron` in AutoClean.yml file)
+ The main subjects of cleaning are those `action commit` which have been existed for 2 day(You could modify this by changing the `value of days_to_expiration`)
+ The main page of cleaning is 10(You could modify this by changing the value of `pages`)
+ Supporting wake by yourself

## Ⅲ.AutoWake.yml
+ Actions File,for wake Leancloud engine caused by flow control
+ The defaut of schedule time is the stander of UTC, every day `0:00` to `15:00` , runs every 16 minutes(You could modify this by changing the value of `-cron` in AutoWake.yml file )
+ Supporting wake by yourself


# Reference
+ [Ching Chow](https://github.com/chingc) put forward the method of cleaning in the question of [`Delete old workflow results`](https://github.community/t/delete-old-workflow-results/16152/2)
+ [wq-h](https://github.com/wq-h) put forward the wake method of Leancloud in the repositroy of [`WakeLeanCloud`](https://github.com/wq-h/WakeLeanCloud)
