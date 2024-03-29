# LeanCloud 流控监督定时任务(Github Action)
[简体中文](https://github.com/ReverseSacle/Auto_Wake_LeanCloud/blob/main/README.md) | [English](https://github.com/ReverseSacle/Auto_Wake_LeanCloud/blob/main/README_EN.md)

# 需求条件
+ 具有一个名为`GITHUB_TOKEN`的Token令牌，需赋予`repo`，`admin:repo_hook` ，`workflow`的权限
+ Token令牌可在头像处点击`Setting`进入后再点击`Developer setting`，最后在`Personal access tokens`点击`Generate new token`即可创建

# 使用方法
+ Fork此仓库后，在此项目的设置中找到`secrets`
+ 之后，在其`Actions secrets`中添加一个名为`SITE`的secret(内容为LeanCloud评论后台地址)
+ 最后在仓库的Actions中查看执行是否正常，并在LeanCloud云引擎处重新部署
+ 另外，若需手动开启`Auto Clean Commit`，可在Actions中的对应action任务中点击`Run workflow`

# 具体内容介绍
## Ⅰ.Get_SiteUrl.py
+ 用于获取评论后台地址内容

## Ⅱ.AutoClean.yml
+ Actions文件，用于清理Action执行过程中产生的commit
+ 执行时间默认为UTC标准(国际时间)，即北京时间周二和周五的凌晨1点(修改-cron元素，即可修改执行时间条件)
+ 主要清理内容为已超过2天的Action commit(可通过修改days_to_expiration变量调控)
+ 主要清理页数为10页(可通过修改pages变量调控)
+ 支持手动唤醒

## Ⅲ.AutoWake.yml
+ Actions文件，用于唤醒因流控关闭的LeanCloud云引擎
+ 执行时间默认为UTC标准(国际时间)，即北京时间早上8点到晚上12点，每16分钟执行一次(修改-cron元素，即可修改执行时间条件)
+ 支持手动唤醒


# 参考
+ [Ching Chow](https://github.com/chingc)在[`Delete old workflow results`](https://github.community/t/delete-old-workflow-results/16152/2)问题中提供的清理方法
+ [wq-h](https://github.com/wq-h)的[`WakeLeanCloud`](https://github.com/wq-h/WakeLeanCloud)仓库中提供的Leancloud唤醒方法
