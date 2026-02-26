# Day 3 - Linux Networking & Web Server Lab

## 📌 Objective

This lab demonstrates Linux networking concepts including connectivity testing, DNS analysis, web hosting, port verification, application testing, firewall configuration, and local DNS resolution.

---

## ✅ Task 1 - Verify Network Configuration

Commands Used:

* `ip a`
* `ip route`
* `hostname -I`

Description:
Verified system IP address, network interface details, and default gateway configuration.

Output Screenshots:

![Task1](Task1.png)
![Task1.2](Task1.2.png)
![Task1.3](Task1.3.png)

---

## ✅ Task 2 - Test Internet Connectivity Flow

Commands Used:

* `ping 8.8.8.8`
* `ping google.com`
* `traceroute google.com`

Description:
Tested internet connectivity and verified DNS resolution and packet routing.

Output Screenshots:

![Task2.0](Task2.0.png)
![Task2.1](Task2.1.png)

---

## ✅ Task 3 - Analyze DNS in Detail

Commands Used:

* `dig google.com`
* `nslookup google.com`

Description:
Analyzed DNS resolution process and observed DNS server response and query time.

Output Screenshots:

![Task3](Task3.png)
![Task3.1](Task3.1.png)

---

## ✅ Task 4 - Host a Simple Website Locally

Commands Used:

* `sudo apt install nginx`
* `echo "Hello from my server" | sudo tee /var/www/html/index.html`
* `curl http://localhost`
* `ip addr`

Description:
Installed Nginx web server and hosted a simple webpage locally. Verified HTTP access using localhost and accessed the website from another browser using the system IP address.

Access Method:

```
http://localhost
http://your_ip
```

Output Screenshots:

(No images for Task 4)

---

## ✅ Task 5 - Check Listening Ports

Commands Used:

* `ss -tuln`
* `sudo systemctl stop nginx`

Description:
Verified that Nginx web server listens on HTTP port 80 and confirmed port removal after stopping the service.

Output Screenshots:

![Task5](Task5.png)
![Task5.1](Task5.1.png)
![Task5.2](Task5.2.png)
![Task5.3](Task5.3.png)
![Task5.5](Task5.5.png)

---

## ✅ Task 6 - Test Application Connectivity

Commands Used:

* `curl -I http://localhost`
* `wget http://localhost`

Description:
Validated web server connectivity by checking HTTP headers and downloading webpage content.

Output Screenshots:

![Task6](Task6.png)
![Task6.1](Task6.1.png)

---

## ✅ Task 7 - Simulate Firewall Restriction (UFW)

Commands Used:

* `sudo ufw enable`
* `sudo ufw allow 80`
* `sudo ufw allow 443`
* `sudo ufw deny 22`
* `sudo ufw status`

Description:
Configured firewall rules to allow web traffic while blocking SSH access.

Output Screenshots:

![Task7](Task7.png)
![Task7.1](Task7.1.png)

---

## ✅ Task 8 - Create a Local Domain Using /etc/hosts

Commands Used:

* `sudo nano /etc/hosts`
* Added entry:

  ```
  127.0.0.1 mytest.local
  ```

Accessed:

```
http://mytest.local
```

Description:
Configured local DNS resolution by mapping a custom domain to localhost using the `/etc/hosts` file.

Output Screenshots:

![Task8](Task8.png)

---

## 🚀 Conclusion

This lab provided hands-on experience with:

* Network configuration verification
* Internet connectivity troubleshooting
* DNS analysis
* Local web hosting
* Port monitoring
* Firewall configuration
* Local DNS mapping

---

**Author:**
Karan Rajesh Dwivedi

