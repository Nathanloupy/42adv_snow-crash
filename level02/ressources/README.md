# Level 02

## Initial Reconnaissance
When browsing the files of the home of level02 user, we can see there is a .pcap file, it's a wireshark file.

```bash
ls -Al
```

```
total 24
-r-x------ 1 level02 level02  220 Apr  3  2012 .bash_logout
-r-x------ 1 level02 level02 3518 Aug 30  2015 .bashrc
-r-x------ 1 level02 level02  675 Apr  3  2012 .profile
----r--r-- 1 flag02  level02 8302 Aug 30  2015 level02.pcap
```

We can download the file on our local machine.
```bash
scp level02@[IP]:level02.pcap .
```
```bash
chmod +r level02.pcap
```

With strings command, we can see mutliple interesting lines :
```bash
strings level02.pcap
```

```
Password: Nf&Nat
Login incorrect
wwwbugs login: df&N
```

We browse the file on this website: https://app.packetsafari.com/. We could have also used Wireshark directly on our local machine.

## Vulnerability Found
In the data of the package 43, we can see 'Password:', let's see the following packages.

In hexadecimal, this is what contains the following packages joined together:

```
66 74 5f 77 61 6e 64 72 7f 7f 7f 4e 44 52 65 6c 7f 4c 30 4c 0d
```

## Exploitation Steps
This corresponds to the following string :

```
f t _ w a n d r [del] [del] [del] N D R e l [del] L 0 L \r
```

Now we can recompose the password :
```
ft_waNDReL0L
```

We can now try to login with the password found.

```bash
su flag02
```

Password: ft_waNDReL0L

We can now execute getflag with user flag02.

```bash
getflag
```

```
Check flag.Here is your token : kooda2puivaav1idi4f57q8iq
```

## Additional Notes

