# Serverless Python

## Prerequisite
* Python 3.8
* serverless.io
* `serverless plugin install -n serverless-python-requirements`

## Create virtual environment
```
$ python3 -m venv .env
```

For VSCode, double-click and `.py` file for VSCode to scan for enviroment. 
Then bring up console in VSCode ` Ctrl+`` `

To use it in regular command line 
```
(MacOS)
$ source .env/bin/activate

(Windows)
$ .\.env\Scripts\activate
```

If this is done correct, we should see (.env) in front of a prompt

```
(.env) ~/p/serverless-python $
```

## Pull in requirements
```
pip install -r requirements.txt
```



## Useful commands
```
$ sls invoke local -f hello           ## Run in local env
$ sls invoke local --docker -f hello  ## This is closer to what will be run on aws
$ sls package
$ sls deploy
```