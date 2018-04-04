#git工作流程









#command
##设置
git config --global user.name "your name"               #设置你的git用户名
git config --global user.email "email@example.com"     #设置你的email地址

##版本库创建
git init                    #创建当前目录为版本库目录，git会在目录下创建.git的隐藏文件夹用来存放git的版本控制文件等

##文件提交至暂存区与版本库
git add <file>              #新增一个文件至暂存区
git commit -m <note>        #提交当前改动并添加注释

##浏览版本控制
git status                  #查看当前git的提交信息
git diff <file>             #查看当前文件与当前HEAD版本库中的差异
git diff ^HEAD -- <file>     #查看当前文件与上个HEAD版本库中的差异
git log                     #查看git commit的历史日志
git log --pretty=oneline    #只显示各版本的版本号

##版本库回滚
git reset --hard <release code/HEAD/HEAD^/HEAD^^>        #将暂存区内容回滚至<版本号/上一个版本/上上一个版本>
git reflog                  #查看回滚日志
git checkout -- <file>      #将工作区内容回滚至版本库

##分支
