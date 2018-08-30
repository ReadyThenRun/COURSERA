### Sales Company:

W.D. Widgets is a small company that sells widgets. They’re mostly made up of salespeople who work with lots of clients. You’ve taken over as the sole IT person for this company of 80-100 people.

When HR tells you to provision a machine for a new employee, you order the hardware directly from a business vendor. You keep one or two machines in stock, in case of emergency. The users receive a username that you generate for them. You then give them an orientation on how to login when they start. You currently manage all of your machines using Windows Active Directory. The company uses only Windows computers. When a new computer is provisioned, you have to install lots of sales-specific applications manually onto every machine. This takes a few hours of your time for each machine. When someone has an IT-related request, they email you directly to help them.

Almost all software is kept in-house, meaning that you’re responsible for the email server, local machine software, and instant messenger. None of the company’s services are kept on the cloud.

Customer data is stored on a single file server. When a new salesperson starts, you also map this file server onto their local machine, so that they can access it like a directory. Whoever creates a folder on this server owns that folder and everything in it. There are no backups to this critical customer data. If a user deletes something, it may be lost for everyone.

The company generates a lot of revenue and is rapidly growing. They’re expecting to hire hundreds of new employees in the next year or so, and you may not be able to scale your operations at the pace you’re working.

### My Answer
There are lots of problem descripted in this question document. 

Firstly, Let the employees to buy computer by themselves is not a good suggestion. They should draft a standard operating procedure (SOP) for procurement process. For a software company, computer have special requirement for then reason that developer will use it as a main weapon to product debugging and software running environment testing. It is essentially for the software company to implement a SOP for computer procurement. 

Secondly, the company should make remediation plans response to the affairs of, for example, facing a computer losing. Company’s computers should be well labelled and well documented. There should be a well-organized inventory system for all the company assets and it is useful in audit affairs.

Thirdly, IT support should help to draft a Standard for Computer OS Management. Building and maintaining optimized corporate computer OS Images. In a software company, developers need lots of professional development tools assistant the software developing process. A new employee may not familiar with those tools which are popularly used in the company. Problems happen when the need for cooperating to finish a task. So, standardize and streamline the process is helpful to save configuring time for setting up a new computer. On another aspect, there are lots of on-hand and well-designed schemes for OS configuring. It is valuable for an IT supporter to learn and overcome this challenge.

Fourthly, the company has not deployed a security Password Management Solution. Unfortunately, employees have to reimage their computer when they are having no way to retrieve their password. A Central Authentication solution can easy solve this problem. As helping employees with password issues is a common task for IT supporter. When an employee lost their password, IT support should help him reset their password to solve the problem.

Fifthly, the company has many of their services in the cloud. They should have a domain controller and central management services such as OpenLDAP, which can track computers connected to the domain. This could be used to provision software to any computers joined to the domain and would implement strict password management.
