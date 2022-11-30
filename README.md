
1. Install python3+ version for this project
2. Configure [virtual](https://virtualenv.pypa.io/en/latest/installation.html#via-pip) env for your OS
3. Activate virtual env
4. `pip install -r requirements.txt `to install dependencies
5. to run tests just run in console `pytest`
6. html report will be generated in the root of dir 

Example of the report

<img width="1670" alt="Screenshot 2022-11-30 at 00 48 37" src="https://user-images.githubusercontent.com/13049374/204674036-4461fa60-311e-4184-bdd8-ead00dd96f30.png">


Query Sample

| articles  | 
| ------------- | 
| ID | 
| AUTHOR  |
| Description  |
| timestamp  |
| Content  |

| tagmap  | 
| ------------- | 
| ID | 
| article_id  |
| tag_id  |


| tag  | 
| ------------- | 
| id | 
| tag_name  |


SELECT *

FROM TABLE articles

INNER JOIN tagmap
  ON articles.id = tagmap.article_id
  
INNER JOIN tagmap
  ON tagmap.tag_id = tag.id
  
WHERE tag.tag_name = 'welcome';
