Instructions to reproduce this tutorial

1. Create directory shaker-service
2. $> cd shaker-service
3. $> npm init -y
4. $> npm install json-server
5. $> echo "node_modules" > .gitignore
6. create file db.json with following contents:

{
  "runs": [
    {
      "project": "https://github.com/apache/dubbo",
      "sha": "f29663bba655c9451b9db75b94d5cf945f0e7901",
      "num-tests" : 401,
      "datetime-epoch": 1620326273,      
      "flakies": [
        {
          "name" : "dubbo-config/dubbo-config-api/src/test/java/org/apache/dubbo/config/event/listener/PublishingServiceDefinitionListenerTest.java",
	  "ratio" : 0.3
	},
	{
	  "name" : "dubbo-config/dubbo-config-api/src/test/java/org/apache/dubbo/config/event/listener/PublishingServiceDefinitionListenerTest.java",
	  "ratio" : 0.7
	}
      ]
    }
  ]
}

7. update package.json and update the scripts section as indicated below:

"scripts": {
  "start": "json-server db.json"
}

8. Try locally:
  8.1 $> npm start
  8.2 access localhost:3000 from the browser

---
Create GitHub repository shaker-service
---