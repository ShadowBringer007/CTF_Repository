# Verify

Downloading the zip file, the contents inside shows the target checksum of the file we are looking for a decrypt script.</br>
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/c3e7220d-453d-4096-a3af-05da51762790)</br>
</br>

Since I am working on a windows machine I opened up a powershell terminal to hash all the files with SHA256. The command used "Get-FileHash * -Algorithm SHA256 | Format-list |Out-file output.txt".
Looking into output.txt for the hash "467A10447DEB3D4E17634CACC2A68BA6C2BB62A6637DAD9145EA673BF0BE5E02", we find that the file "c6c8b911" contains the right content.
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/f008c803-2084-45cc-b22a-5e083470cb06)</br>
</br>

Connecting to the server we can run decrypt.sh with argument c6c8b911 and the flag is presented.</br> 
![image](https://github.com/ShadowBringer007/CTF_Repository/assets/47370367/eb68a4d7-8150-476e-9a69-f8740468a0e9)</br>

