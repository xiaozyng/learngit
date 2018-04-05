#git工作流程

git分为三个区，分别为 工作区(work),暂存区(stage),主分支(master)。
提交顺序为：

work --add--> stage --commit--> master

#command
##设置
git config --global user.name "your name"               #设置你的git用户名
git config --global user.email "email@example.com"     #设置你的email地址

##版本库创建
git init                    #创建当前目录为版本库目录，git会在目录下创建.git的隐藏文件夹用来存放git的版本控制文件等

##提交与删除
git add <file>              #新增一个文件至暂存区
git commit -m <note>        #提交当前改动至master并添加注释
git commit -am <note>       #相当于add + commit -m
git rm <file>               #删除一个文件

##状态以及日志浏览
git status                  #查看当前git的提交信息
git diff <file>             #查看当前文件与当前HEAD版本库中的差异
git diff ^HEAD -- <file>     #查看当前文件与上个HEAD版本库中的差异
git log                     #查看git commit的历史日志
git log --pretty=oneline    #只显示各版本的版本号

##版本库回滚
git reset --hard <release code/HEAD/HEAD^/HEAD^^>        #将暂存区内容回滚至<版本号/上一个版本/上上一个版本>
git reflog                  #查看回滚日志
git checkout -- <file>      #将工作区内容回滚至master最新版本

##分支
git branch                 #查看当前分支信息
git branch <分支名>        #创建分支
git checkout <分支名>      #切换到分支
git checkout -b <分支名>   #相当于branch + checkout ，创建分支并切换至对应分支
git merge <分支名>         #合并分支至master
git branch -d <分支名>     #删除分支

##远程仓库
ssh-keygen -t rsa -C "email@example.com"        #生成非对称密钥
git remote add origin https://github.com/xiaozyng/learngit.git          #在本地添加远程仓库
git push -u origin master       #首次push本地master至远程仓库，-u参数表示将此分支与远程仓库的做关联，之后的push、pull不需要再指定upstream，git就会自动的将找到对应分支。
git pull origin [分支]          #pull
git push oragin :<分支>         #删除远程仓库分支