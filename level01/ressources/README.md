# Level 01

## Initial Reconnaissance
When browsing the files of the machine, we can see that flag01 is the only user that has a password field not set to x.

```bash
cat /etc/passwd
```

```
flag01:42hDRfypTqqnw:3001:3001::/home/flag/flag01:/bin/bash
```

## Vulnerability Found
'42hDRfypTqqnw' looks like a hash from DES crypt of a weak password.

## Exploitation Steps
With a simple python script, we can decrypt the hash.

```bash
python3 rainbow.py
```

```
Attempting to crack hash: 42hDRfypTqqnw
Trying common passwords...

🎉 PASSWORD FOUND: abcdefg
```

We can now try to login with the password found.

```bash
su flag01
```

Password: abcdefg

We can now execute getflag with user flag01.

```bash
getflag
```

```
Check flag.Here is your token : f2av5il02puano7naaf6adaaf
```

## Additional Notes

An alternative way to solve this level is to use john the ripper tool. The hint was given by the files names during the level00.
