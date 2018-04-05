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
git log --graph             #显示图形化log
git log --abbrev-commit     #显示短的commit code
git show [tag|file]         #显示tag|file的详细信息

##版本库回滚
git reset --hard <release code/HEAD/HEAD^/HEAD^^>        #将暂存区内容回滚至<版本号/上一个版本/上上一个版本>
git reflog                  #查看回滚日志
git checkout -- <file>      #将工作区内容回滚至master最新版本

##分支
git branch                  #查看当前分支信息
git branch <分支>           #创建分支
git branch --set-upstream <分支> <origin/分支>          #将本地分支与远程仓库的一个分支关联
git checkout <分支>         #切换到分支
git checkout -b <分支>      #相当于branch + checkout ，创建分支并切换至对应分支
git checkout -b <分支> <origin/分支>  #在本地创建与远程仓库关联的分支，并且还至创建的本地分支
git branch -d <分支>        #删除分支
git branch -D <分支>        #强制删除未合并的分支，使用此选项会产生数据丢失的结果。
git merge <分支名>          #合并分支至master
git merge --no-ff  -m <note> <分支>       #普通模式合并,合并后Log可以看出合并历史

##储存内容
git stash                       #将当前工作区内容存储起来，暂存区会取回工作区后储存
git stash list                  #显示当前储存的内容信息
git stash pop [stash@{0}]       #释放存储的内容，并将存储区的对应内容删除，stash@{0}、stash@{1}...代表多次存储时每个存储内容的标识，可以自由选择释放哪个存储
git stash allpy [stash@{0}]     #释放存储的内容，但是不将存储区的对应内容删除
git stash drop [stash@{0}]      #与allpy搭配使用，手动删除存储区的内容

##远程仓库
ssh-keygen -t rsa -C "email@example.com"        #生成非对称密钥
git remote add origin https://github.com/xiaozyng/learngit.git          #在本地添加远程仓库
git remote -v                   #显示远程仓库的信息，-v 详细信息
git push -u origin master       #首次push本地master至远程仓库，-u参数表示将此分支与远程仓库的做关联，之后的push、pull不需要再指定upstream，git就会自动的将找到对应分支。
git pull origin [分支]          #pull
git push origin :<分支>         #删除远程仓库分支

##标签管理
git tag                             #查看所有tag信息
git tag -m <note> <tag> <commit code>          #添加一个tag，-m 添加注释；-s 添加gpg key认证；commit code可以为之前的版本添加tag；
git tag -d <tag>                    #删除一个tag
git tag -a <tag> -m <note>          #为一个指定tag添加注释信息
git push origin <tag>               #推送某个标签至远程仓库
git push origin --tags              #推送所有标签至远程仓库
git push origin :refs/tags/<tag>    #删除远程仓库上的某个标签，需要先tag -d删除本地标签后，才能删除远程仓库的标签

gpg --gen-key                       #创建pgp key，交互型命令
gpg --list-keys                     #列出所有的pgp keys
git tag -m <note> -s <tag> -u <pgp key uid>     #新建标签添加gpg key认证
git tag -v <tag>                    #调用gpg验证key，如key匹配，则会显示具体的key的信息

