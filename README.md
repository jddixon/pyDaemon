# py_daemon
## Daemon Behavior

Per W Richard Stevens, "Unix Network Programming", and
[PEP 3143](https:/www.python.org/dev/pwpa/pwp-3143),
basic daemon behavior includes

1 closing all open file descriptors
1 changing current working directory
1 resetting the file access creation mask
1 running in the background
1 disassociation from the process group
1 ignoring terminal i/o signals
1 disassociation from control terminal
1 not reacquiring a control terminal
1 and correctly handling:

* being started by the System V init process
* being terminated by a `SIGTERM` signal
* `SIGCLD` signal generation by children

PEP 3143 also encourages emulating the
[slack daemon](http://libslack.org/manpages/daemon.3.html) and

1 setting up a corrects process context for a daemon
1 behaving sensibly when started by initd or inetd
1 revoking any suid or sgid privileges
1 optionally preventing genertion of core files
1 optionally naming the daemon by creating and locking a PID file, guaranteeing
    that only one daemon of that name can run at a given time
1 optionally setting the daemon's user and group ID to root
1 optionally creating a chroot jail
1 optionally redirecting stdout and stderr to syslog


## On-line Documentation

More information on the **py_daemon** project can be found
[here](https://jddixon.github.io/py_daemon)
