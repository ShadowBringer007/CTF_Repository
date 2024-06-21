# Commitment Issues WriteUp

The download file we are given is a github repo with only messages.txt in it.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/2ff38c00-f973-4c81-bda7-6218dde35643)</br>
</br>

Since this is a github repo, (I will be running in git bash), I will run the command "git log" to show all commits. Seeing the first commit is the flag creation.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/150c915c-584a-43dd-a3aa-8a8b896634a4)</br>
</br>

To access the that particular commit, I will run "git show e720dc26". e720dc26 is the first 8 characters of the hash from the result of "git log" command. When doing this it shows everything in the file during the first commit which contains the flag.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/8773bea9-a5f1-4eec-83a9-21f6022505cc)
