# Level 09

## Initial Reconnaissance
When browsing the files of the home of level09 user, we can see there is binary file called level09 owned by level09 and a file called token owned by flag09.

```bash
ls -Al
```

```
total 24
-r-x------ 1 level09 level09  220 Apr  3  2012 .bash_logout
-r-x------ 1 level09 level09 3518 Aug 30  2015 .bashrc
-r-x------ 1 level09 level09  675 Apr  3  2012 .profile
-rwsr-sr-x 1 flag09  level09 7640 Mar  5  2016 level09
----r--r-- 1 flag09  level09   26 Mar  5  2016 token
```

```
level09@SnowCrash:~$ ./level09 
You need to provied only one arg.
level09@SnowCrash:~$ cat token 
f4kmm6p|=�p�n��DB�Du{��
level09@SnowCrash:~$ hexdump -C token 
00000000  66 34 6b 6d 6d 36 70 7c  3d 82 7f 70 82 6e 83 82  |f4kmm6p|=..p.n..|
00000010  44 42 83 44 75 7b 7f 8c  89 0a                    |DB.Du{....|
0000001a
```

Let's get the binary and the token on our local machine and pass it through a binary analysis tool on : https://dogbolt.org/.

```bash
scp -P 4242 level09@[IP]:level09 .
scp -P 4242 level09@[IP]:token .
chmod +r token
```

```c
while (true)
{
    var_120 += 1;
    int32_t i = 0xffffffff;
    int32_t edi_1 = argv[1];
    
    while (i)
    {
        bool cond:0_1 = 0 != *edi_1;
        edi_1 += 1;
        i -= 1;
        
        if (!cond:0_1)
            break;
    }
    
    if (var_120 >= ~i - 1)
        break;
    
    putchar(*(var_120 + argv[1]) + var_120);
}

result = fputc(0xa, stdout);
```

## Vulnerability Found
It looks like the binary is simply transforming the string and then printing it.

## Exploitation Steps
With a simple python script, we can reverse the logic.

```bash
python3 reverse.py
```

```
Decrypted password: f3iji1ju5yuevaus41q1afiuq
Verification - re-encrypting the password:
Re-encrypted: 'f4kmm6p|=\x82\x7fp\x82n\x83\x82DB\x83Du{\x7f\x8c\x89'
Original token: 'f4kmm6p|=\x82\x7fp\x82n\x83\x82DB\x83Du{\x7f\x8c\x89'
Match: True
```

```bash
su flag09
```

Password: f3iji1ju5yuevaus41q1afiuq

```bash
getflag
```

```
Check flag.Here is your token : s5cAJpM8ev6XHw998pRWG728z
```

## Additional Notes

