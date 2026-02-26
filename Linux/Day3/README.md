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

* Task1/ip-address.png
* Task1/ip-route.png

---

## ✅ Task 2 - Test Internet Connectivity Flow

Commands Used:

* `ping 8.8.8.8`
* `ping google.com`
* `traceroute google.com`

Description:
Tested internet connectivity and verified DNS resolution and packet routing.

Output Screenshots:

* Task2/ping-ip.png
* Task2/ping-domain.png
* Task2/traceroute.png

---

## ✅ Task 3 - Analyze DNS in Detail

Commands Used:

* `dig google.com`
* `nslookup google.com`

Description:
Analyzed DNS resolution process and observed DNS server response and query time.

Output Screenshots:

* Task3/dig-output.png
* Task3/nslookup-output.png
* Task3/dns-failure.png

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

* Task4/nginx-install.png
* Task4/localhost-test.png
* Task4/ip-address.png
* Task4/browser-access.png

---

## ✅ Task 5 - Check Listening Ports

Commands Used:

* `ss -tuln`
* `sudo systemctl stop nginx`

Description:
Verified that Nginx web server listens on HTTP port 80 and confirmed port removal after stopping the service.

Output Screenshots:

* Task5/port80-running.png
* Task5/port80-stopped.png

---

## ✅ Task 6 - Test Application Connectivity

Commands Used:

* `curl -I http://localhost`
* `wget http://localhost`

Description:
Validated web server connectivity by checking HTTP headers and downloading webpage content.

Output Screenshots:

* Task6/curl-output.png
* Task6/wget-download.png

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

* Task7/ufw-enabled.png
* Task7/ufw-status.png
* Task7/connectivity-test.png

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

* Task8/hosts-file.png
* Task8/ping-mytest.png
* Task8/browser-access.png

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
B.Tech CSE (AI & ML)
