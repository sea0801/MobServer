#About
this is a server providing  app download and installation.support Android and iOS.<br/>
https is required,so make sure that having genreated crts

#Requirements
Python 2.7+<br/>
Tornado Module

#Usage
1.set config in config dir,set your ip<br/>
2.generate crt files<br/>
    1.生成自己的密钥对:openssl genrsa -out ca.key 1024 <br/>
    2.生成证书请求文件，并使刚刚的key来加密CA根证书:openssl req -new -x509 -days 365 -key ca.key -out ca.crt<br/>
    3.生成服务器使用的证书，并用自己的根证书签名:openssl genrsa -out server.key 1024  <br/>
    4.生成证书请求文件:openssl req -new -key server.key -out server.csr <br/>
    5.接下来我们需要使用根证书对这个证书进行签名，但是在签名之前，需要做一些准备工作， 我们需要构建这样一个目录结构，在当前目录新建文件夹demoCA，
进入demoCA，在demoCA下创建两个文件index.txt和serial ，以及文件夹newcerts，其中index.txt的内容为空，serial的内容为01。
完成之后<br/>
    6.开始签名:openssl ca -in server.csr -out server.crt -cert ca.crt -keyfile ca.key <br/> 
    
3.set crts path in main.py<br/>
4.copy ca.crt to static dir<br/>
5.run the server: python main.py<br/>

#Tdo
1.add upload api
2.add upload web


    
