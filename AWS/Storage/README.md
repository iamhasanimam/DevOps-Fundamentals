AWS provides three distinct cloud storage types to meet diverse requirements and application needs

Block storage

Block storage provides persistent, low-latency block-level storage volumes that attach to EC2 instances like physical hard drives. Block storage volumes can be encrypted, backed up via snapshots, and modified while in use without disrupting the instance. AWS offers two primary block storage services:

Amazon EC2 instance store
An unmanaged non-persistent, high-performance block storage directly attached to EC2 instances for temporary data.

Amazon Elastic Block Store (EBS)
A managed service that provides persistent block storage volumes for EC2 instances, offering various types for different workloads

Object Storage

Object storage is a data storage architecture that manages data as objects in a flat address space. It offers unlimited scalability so you can store vast amounts of unstructured data without worrying about capacity constraints. Object storage provides enhanced metadata capabilities to provide more efficient data management, search, and analytics across massive datasets.

The following is the primary AWS object storage service:

Amazon Simple Storage Service (S3)
A fully managed scalable object storage service for storing and retrieving any amount of data from anywhere.

Object = data + unique id + metadata best for videos

File storage

File Storage : Cloud based access through shared file system

AWS file storage services provide shared file systems accessible over networks, so multiple users and applications can access the same data simultaneously. They offer scalability and flexibility so you can expand storage capacity as needs grow without managing physical infrastructure. AWS offers two primary file storage services:

Amazon Elastic File System (EFS)
A fully managed, scalable NFS file system for use with AWS Cloud services and on-premises resources.

Amazon FSx
A fully managed file storage services for popular file systems like Windows, Lustre, and NetApp ONTAP.


Additional storage services

These services don't fit cleanly into the categories we've defined so far, but they're important AWS storage offerings that you should be familiar with.

AWS Storage Gateway
A fully managed, hybrid-cloud storage service that provides on-premises access to virtually unlimited cloud storage.

AWS Elastic Disaster Recovery
A fully managed service that streamlines the recovery of your physical, virtual, and cloud-based servers into AWS.
