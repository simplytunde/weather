#Setting up SSH Access

In this document, we will be talking about how to setup ssh access for all employees at a company. It is recommended to use a configuration management system like chef for this. Some of the best practices that must be followed when implementing ssh key management includes;

+ Active Management of all ssh keys to ensure we keep track of active keys.
+ Principle of least privilege.
+ Key Rotation.
+ Avoid Hard code SS Keys.

## Chef

To setup ssh for  employees in the company; 

### Adding user SSH keys

1. Operators must write script that generates ssh key for  company employee with the principle of one key per user. The private key should be shared with the employee via secure link or an encrypted s3 bucket for download.

2. The generated public key will be stored in an encrypted bucket with only privileged access or encrypted databag.

3. Since we are using chef for configuration management on our servers and assuming users access on services are managed by group membership, we write chef recipe that adds ssh key for each user. Something like this;

   ```chef
   users.each do |name, ssh_key|
     ssh_authorize_key name do
       key ssh_key['key']
       user ssh_key['user']
     end
   end
   ```

   

4. Once our change is applied, chef client picks it up and add the ssh key to appropriate servers.

### Removing user SSH keys

1. We can  write a script that removes the user ssh public key from chef as well as removes the user from appropriate  server based on groups.
2. We apply our change and once chef client runs on the node, it removes the key from the node `authorized_keys` file

