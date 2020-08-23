rasa_path='./rasa'
config_path=$rasa_path'/config.json'
project_path=$rasa_path'/projects'
python -m rasa_nlu.server --config $config_path --path $project_path