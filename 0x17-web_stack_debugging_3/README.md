webstack debugging

-run ps aux | grep apache
-sudo strace -p <pid of the apache service>
then move to the other window and curl -sI on localhost

