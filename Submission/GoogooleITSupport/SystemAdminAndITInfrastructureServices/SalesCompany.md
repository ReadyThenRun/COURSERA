### Sales Company:

W.D. Widgets is a small company that sells widgets. They’re mostly made up of salespeople who work with lots of clients. You’ve taken over as the sole IT person for this company of 80-100 people.

When HR tells you to provision a machine for a new employee, you order the hardware directly from a business vendor. You keep one or two machines in stock, in case of emergency. The users receive a username that you generate for them. You then give them an orientation on how to login when they start. You currently manage all of your machines using Windows Active Directory. The company uses only Windows computers. When a new computer is provisioned, you have to install lots of sales-specific applications manually onto every machine. This takes a few hours of your time for each machine. When someone has an IT-related request, they email you directly to help them.

Almost all software is kept in-house, meaning that you’re responsible for the email server, local machine software, and instant messenger. None of the company’s services are kept on the cloud.

Customer data is stored on a single file server. When a new salesperson starts, you also map this file server onto their local machine, so that they can access it like a directory. Whoever creates a folder on this server owns that folder and everything in it. There are no backups to this critical customer data. If a user deletes something, it may be lost for everyone.

The company generates a lot of revenue and is rapidly growing. They’re expecting to hire hundreds of new employees in the next year or so, and you may not be able to scale your operations at the pace you’re working.

### My solution:
Firstly, I will think about to make full use of the advantage of Group Policy Management tools and set up well functional optimized GPOs. It is an effective way to manage user accounts. We can enforce the complexity requirements of passwords of user login accounts to promote the safety level of our whole company.

Secondly, just like the condition we are facing in the first software company, we can build and maintain a well optimized corporate computer OS Images which some of the working software were pre-installed. So, we can save the workload in the next time when we provide a new computer.

Thirdly, as we all know that the sensitive custom data should have its backups. We should have short time cycle backup schema and worked with long-time cycle backup schema. What's more, we should not only backup those files only on our local machine. We can buy a security file backup service on a reliable third-party cloud platform or purchase other separate working storage hardware, avoiding the data lost in the potential of hardware physical damage conditions.

Fourthly, I will use the attribute of GPOs set different file access permission. Only domain admins who have the permission of full control of files and directory can delete files on the file server. All users could be assigned permissions based on roles in the company and corresponding GPOs.

Fifthly, the company is growing rapidly, we can apply more investment in system infrastructure and human resources. We can move more workload to a third-party platform and suggest the company hire more employee on IT support. 

