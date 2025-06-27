# Level 00

## Initial Reconnaissance
First, let's connect to the machine with user level00 through ssh.

```bash
ssh level00@[IP]-p 4242
```

Password: level00

We need to execute getflag with user flag00. Let's check the files owned by flag00.

```bash
find / -user flag00 2>/dev/null
```

We can see that the two files are owned by flag00.

```bash
/usr/sbin/john
/rofs/usr/sbin/john
```

Let's check the content of the files.

```bash
cat /usr/sbin/john
cat /rofs/usr/sbin/john
```

We can see that the two files are the same.

```bash
cdiiddwpgswtgt
```

## Vulnerability Found

The content looks like a password passed through a Caesar cipher.
With this website : https://www.dcode.fr/caesar-cipher, we can decrypt the password.

## Exploitation Steps

The only word that makes sense is "nottoohardhere".

```bash
su flag00
```

Password: nottoohardhere

We can now execute getflag with user flag00.

```bash
getflag
```

```bash
flag00@SnowCrash:~$ getflag
Check flag.Here is your token : x24ti5gi3x0ol2eh4esiuxias
```

## Additional Notes
