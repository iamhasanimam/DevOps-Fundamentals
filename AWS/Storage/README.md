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


Block level storage :  a place to store file , it updates the pieces that change 


#### Amazon EC2 instance store

Amazon EC2 instance store isn't a stand-alone AWS block storage service. Rather, it refers to the block-level storage that is physically attached to the EC2 instance host computer. Depending on the type of instance, EC2 instance store might come attached as the default storage. Since its data is lost when an instance is stopped or terminated, EC2 instance store is best for temporary memory-based storage needs like buffers, caches, and scratch data. It is not recommended for applications that require data retention.

Key takeaway: no data persistence

An Amazon EC2 instance store provides temporary block-level storage for an Amazon EC2 instance. This means that if you stop or terminate an Amazon EC2 instance, all the data written to the attached instance store is deleted.


#### Amazon Elastic Block Store (EBS)

Amazon EBS provides persistent block-level storage volumes for use with Amazon EC2 instances. EBS volumes act like external hard drives, offering consistent and low-latency performance for workloads like databases and file systems.

EBS volumes can be conveniently backed up, resized, and attached to different EC2 instances. To create an EBS volume, you define the configuration for things like volume size and type. After the volume has been created, it can be attached to an Amazon EC2 instance. Because EBS volumes are for data that needs to persist, it’s important to back up the data. It's recommended that you take incremental backups of EBS volumes by creating Amazon EBS snapshots.

Key takeaway: data persistence

Amazon EBS provides block-level storage volumes that you can use with Amazon EC2 instances. If you stop or terminate an Amazon EC2 instance, all the data on the attached EBS volume remains available.

#### Amazon EBS snapshot

EBS snapshots are point-in-time backups of EBS volume. They can be used for disaster recovery, data migration, volume resizing, and for creating consistent backups of production workloads. EBS snapshots are incremental, so they only save the blocks on the volume that have changed after your most recent snapshot.

EBS snapshots can be used to create multiple new volumes, and new volumes created from a snapshot are an exact copy of the original volume at the time the snapshot was taken. Snapshots of EBS volumes are stored redundantly in multiple Availability Zones using Amazon S3.  

#### Amazon Data Lifecycle Manager

You can automate the creation, retention, and deletion of EBS snapshots using Amazon Data Lifecycle Manager. Amazon Data Lifecycle Manager can schedule snapshots during off-peak hours to minimize performance impact and automatically delete outdated backups to control storage costs. It's particularly valuable for large-scale deployments where manual snapshot management would be time-consuming and error-prone.


___

Amazon S3 is an object storage service that can store unlimited amounts of data in the AWS Cloud. Object storage is particularly well-suited for handling large amounts of unstructured data, such as documents, images, and videos. In this lesson, you will explore some of the core functionality and practical use cases of Amazon S3.

#### Amazon Simple Storage Service (S3)

Amazon S3 is a fully managed, highly-available object storage service for storing and retrieving any amount of data as objects. It offers 99.999999999 percent durability, meaning your data is highly protected against loss, and offers features like versioning, lifecycle management, and various storage classes to optimize costs.

Amazon S3 stores files as objects in containers known as buckets, and each object can range in size from a few bytes to several terabytes. It integrates seamlessly with other AWS services and supports a wide range of use cases, from basic backups to complex data lakes.

##### S3 objects
An object in Amazon S3 is the fundamental unit of data storage. When you upload a file to Amazon S3, it becomes an object and is stored durably across multiple facilities within your chosen Region.

Each object typically includes the data itself, metadata, and a unique identifier, or key. Objects can be of any file type, such as images, videos, documents, or application data, and can range in size from a few bytes to several terabytes.

Each Amazon S3 object is uniquely identified within a bucket by its key, which is essentially its file name. Objects also have properties like version ID, access control information, and user-defined metadata.

##### S3 buckets
An S3 bucket is a container for storing objects in Amazon S3. Buckets have a globally unique name across all of AWS, which helps to identify and organize your stored data.

Buckets serve as the basic unit for access control and can hold a virtually unlimited number of objects. They play a crucial role in data management by making it possible to group related objects and apply policies at the bucket level.

When creating a bucket, you specify its name and the Region where it will reside. Buckets can be configured with various settings, including versioning, logging, and access permissions.

Amazon S3 supports a wide range of use cases for both cloud-based applications and traditional on-premises workloads. Amazon S3 is commonly used for content distribution, hosting static websites, and delivering media files. It's also a popular choice for things like application data storage, archiving, data lakes, and compliance-driven data retention.


#### Amazon S3 Storage Classes and S3 Lifecycle

S3 Lifecycle

To avoid manually managing your object storage tier configurations, you can use S3 Lifecycle configurations to automate the process. When you define a lifecycle configuration for an object or group of objects, you can choose to automate between two types of actions, as follows:

Transition actions: define when objects should transition to another storage class.

Expiration actions: define when objects expire and should be permanently deleted.

For example, you might transition objects to S3 Standard-IA storage class 30 days after you create them. Or you might archive objects to the S3 Glacier Deep Archive storage class 1 year after creating them.


#### Amazon Elastic File System (EFS)

Amazon EFS is a fully managed, scalable file storage service for use with AWS cloud services and on-premises resources. It operates using the Linux Network File System (NFS) protocol, and automatically scales to petabytes as you add or remove files without disrupting applications. EFS is designed to support a wide variety of workloads and can be accessed by multiple EC2 instances simultaneously.

##### Amazon EFS storage classes

With Amazon EFS, you can create and configure file systems quickly without any minimum fee or setup cost. You pay only for the storage used and you can choose from a range of storage classes designed to fit your use case.

The EFS Standard and EFS Standard-Infrequent Access (Standard-IA) storage classes offer Multi-AZ resilience and the highest levels of durability and availability. They have a higher cost associated with them due to higher availability and durability.

The EFS One Zone and EFS One Zone-Infrequent Access (EFS One Zone-IA) provide additional savings by saving your data in a single Availability Zone. By using just one Availability Zone, you can reduce your storage costs when compared to the Standard EFS storage classes.

The EFS Archive storage class is cost-optimized for data that is accessed only a few times a year or less and that does not need the sub-millisecond latencies of EFS Standard. EFS Archive offers a storage price up to 50% lower compared to EFS Infrequent Access, providing a more cost-optimized experience for cold, rarely-accessed data.

#### Amazon FSx for Windows File Server

Amazon FSx for Windows File Server provides fully managed shared storage built on Windows Server. It delivers a wide range of data access, data management, and administrative capabilities.

Use cases include the following:

Migrate Windows file servers to AWS.

Accelerate hybrid workloads.

Reduce SQL Server deployment cost.

Streamline virtual desktops and streaming.

#### AWS Storage Gateway

Storage Gateway is a hybrid cloud storage service that makes it possible to seamlessly integrate on-premises environments with AWS Cloud storage. You can use it to extend your local storage to the cloud while maintaining low-latency access to frequently used data.

You can use Storage Gateway to streamline storage management and reduce costs for practical hybrid cloud storage use cases. These include moving backups to the cloud, using on-premises file shares backed by cloud storage, and providing low-latency access to data in AWS for on-premises applications.

#### Disaster Recovery

Elastic Disaster Recovery replicates critical workloads to AWS with minimal downtime. Your servers' block-level data is continuously replicated to AWS, making it ideal for uses that require robust disaster recovery solutions. It supports both physical and virtual servers to enable rapid recovery during disruptions, which is particularly valuable for industries like healthcare where system availability is crucial.

You can use Elastic Disaster Recovery to reduce downtimes and data loss while eliminating the costs associated with maintaining secondary data centers. It also offers non-disruptive disaster recovery testing, meaning it's capable of quickly launching recovery instances when needed.