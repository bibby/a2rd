# a2rd

Generates a [RunDeck](http://rundeck.org/) Resource YAML from [ansible](http://www.ansible.com/home) facts gathered from an inventory file.

The conversion is by no means complete, but enough to at least import an inventory into rundeck with the correct hostnames and architectures.

Modify for your own needs; improvements and suggestions welcomed.

## Use
```
a2rd [hosts_file [out_file]]
  hosts_file - (default: hosts.ini) ansible hosts ini
  out_file - (default: rundeck-resources.yml) rundeck resources yaml output
```

## License 

[Creative Commons CC0 1.0 Universal (CC-0)](https://www.tldrlegal.com/l/cc0-1.0)