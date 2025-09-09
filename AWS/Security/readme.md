### AWS Identity and Access Management (IAM)

Securely manage identities and access to AWS services and resources.

One of the best ways to prevent security incidents before they happen is through proper permission and access management. With IAM, by default, all actions are denied. You must explicitly grant permission to someone before they can perform any actions in your account.

When you grant permissions, you should provide access only on a need-to-have basis. This concept is called the principle of least privilege.


The principle of least privilege dictates that you should only give people and systems access to what they need and nothing else.

#### AWS IAM Identity Center

IAM Identity Center centralizes identity and access management across AWS accounts and applications. IAM Identity Center can also connect to an existing identity source and provide your workforce with single sign-on access to all your connected AWS services and accounts. This is called federated identity management.

Federated identity management is a system that allows users to access multiple applications, services, or domains using a single set of credentials.

#### AWS Secrets Manager

Secrets Manager provides a secure way to manage, rotate, and retrieve database credentials, API keys, and other secrets throughout their lifecycle. This helps keep your applications, services, and IT resources safe.

Secrets are confidential or private information intended to be known only to specific individuals or groups. Examples include passwords, database credentials, and API keys

#### AWS Systems Manager

Systems Manager provides a centralized view of nodes across your organization’s accounts and Regions and multi-cloud and hybrid environments. With this service, you can quickly access node information, such as ID and operating system details, and automate registry edits, user management, and security patching.

Nodes are connection points in a network, system, or structure.


AWS IAM 
User
Groups
Policies
Roles

#### Network and application attacks

Network and application protection is another vital component of a secure environment on AWS. In the previous video, you learned about denial of service attacks that might be used against your enterprise.

#### DoS attacks
In a denial of service attack, an attacker floods a web application with excessive network traffic. Legitimate customer requests are denied if the web application becomes overloaded and can no longer respond.

#### DDoS attacks
In a distributed denial of service (DDoS) attack, an attacker can use multiple infected computers (called zombie bots) to unknowingly send excessive traffic to a web application.

#### AWS network and application protection

AWS automatically protects against low-level, brute-force attacks, such as DDoS, through its built-in infrastructure and network architecture. AWS infrastructure reaches across the globe and includes multiple Regions, Availability Zones, and edge locations. It is designed to make it difficult for attackers to overwhelm the system.

It does by Security Groups, ELB and and AWS regions

WS protection through services

AWS also offers the following services to help protect your network and applications.


#### AWS Shield

AWS Shield Standard is designed to automatically protect AWS customers from the most common, frequently occurring types of DDoS attacks at no cost. It uses a variety of analysis techniques to detect and mitigate incoming malicious network traffic in real time.

AWS Shield Advanced is a paid service that provides detailed attack diagnostics and the ability to detect and mitigate sophisticated DDoS attacks. It also integrates with other services, such as Amazon CloudFront, Amazon Route 53, and ELB.

Additionally, you can integrate AWS Shield with AWS WAF by writing custom rules to mitigate complex DDoS attacks.

#### AWS WAF

AWS WAF is a web application firewall that monitors network requests that come into your web applications. When a request comes into AWS WAF, it checks the IP address against a web access control list (web ACL). If the request comes from a blocked IP address on the web ACL, AWS WAF denies access. Legitimate requests are allowed access.

#### Data encryption

So much of what you do on AWS is driven by data. Keeping your data safe is important to make sure your applications run smoothly and to maintain customer trust.

Encryption is a key component of data protection. Let's review how data encryption works.

#### Encryption basics
Data encryption works like a lock and key mechanism. If you have the right key, you can access the encrypted data. Otherwise, you cannot access the data. For example, let's say you are protecting a customer's profile. An encryption key is used to turn the profile information into a randomized set of characters. A decryption key is used to access the customer's information, such as their name, only when it's needed by your application.

### Types of data encryption

Data encryption comes in the following two forms: 

Data encryption at rest: The data is idle and not moving, like when it's stored in a database.

Data encryption in transit: The data is moving between locations, like when it's being sent from a database to an application. SSL/TLS certificates are used to establish encrypted network connections from one system to another.


#### AWS data protection

AWS has a variety of methods for protecting data. They include built-in data protection for storage options and services specifically designed for enhanced data protection.

Let's review some of the data protection methods. 


AWS built-in data protection

Amazon S3
By default, all new S3 buckets have encryption configured, and all uploaded objects are encrypted at rest.

Amazon EBS

Amazon EBS volumes and snapshots can be encrypted at rest, including both boot and data volumes of an Amazon EC2 instance.


Amazon DynamoDB

Server-side encryption at rest is enabled on all DynamoDB table data using encryption keys stored in AWS Key Management Service (AWS KMS).

AWS data protection services

AWS also offers the following services to help protect your data.


#### AWS Key Management Service (AWS KMS)

You can use AWS KMS to create and manage cryptographic keys. These keys can then be used to encrypt and decrypt your data. You can also control the use of keys across a wide range of services and in your applications. For example, you can specify which IAM users and roles can manage keys. Your keys never leave AWS KMS, and you can temporarily disable them so they can no longer be used.

A cryptographic key is a random string of digits used for locking (encrypting) and unlocking (decrypting) data

#### AWS Certificate Manager (ACM)

ACM centralizes the management of your SSL/TLS certificates that provide data encryption in transit. It can be used to protect various AWS services and your connected on-premises resources.

SSL/TLS certificates are used to establish encrypted network connections from one system to another.