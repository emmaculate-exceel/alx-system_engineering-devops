<h1> Firewall </h1>
<h2> guides on how to fix your firewall project on task 0 and the advance task </h2>

<h3> task 0</h3>
* all you have to do according to task one is just to
follow the instructions and you'll be fine .
which simply means the checker will definite check for the task one
<h3> Note: you'll have to do this one the server too other wise you'll have
a blocker </h3>

<h3> advance task</h3>
Note : redirectig traffic between ports
login into your webserver then
sudo vi /etc/ufw/sysctl.conf
then uncomment this line #net/ipv4/ip_forward=1
then save the configuration file and exit

Next thing  to do is to apply changes using the command sudo sysctl -p
then --> sudo ufw allow 8080/tcp
Next --> sudo vi /etc/ufw/before.rules
then add this configuration right after the *filter line
add this configuration to the next 3 lines of the config file
*nat
:PREROUTING ACCEPT [0:0]
-A PREROUTING -p tcp --dport 8080 -j REDIRECT --to-port 80
COMMIT

then save the config file and
disable the firewall --> sudo ufw disable
the enable firewall --> sudo ufw enable

then you can logout