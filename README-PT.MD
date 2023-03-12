# messages-web-service
Pequena aplicação web Resftull feita como trabalho prático na aula de sistemas distribuídos. O objetivo foi evitar o uso de frameworks que melhorem o nível de abstração, em vez disso, várias bibliotecas de baixo nível foram usadas para desenvolver este projeto.

## API endpoints
A API do backend que permite a integração com o frontend utiliza arquivos JSON para a comunicação e possui os seguintes endpoints que seguem os seguintes formatos:
- GET
  - /message - retorna todas as mensagens que já foram enviadas no sistema, independente de que enviou ou recebeu;
  - /message?message_id=4 - retorna a mensagem que possui o id igual a 4 ou retorna um erro caso não exista mensagem com esse id;
  - /message?sender_email=example@example.com - retorna enviadas por um determinado usuário que possui o endereço de email informado, nesse caso example@example.com;
  - /message?recipient_email=example@example.com - retorna todas as mensagens recebidas por um determinado usuário que possui o endereço de email informado, nesse caso example@example.com;
  - /user - retorna todos os usuários cadastrados no sistema;
  - /user?user_id=3 - retorna o usuário cujo id é igual ao id informado na requisição;
  - /user?email_address=example@example.com - retorna o usuário cujo endereço de email é igual ao endereço de email informado na requisição;
- POST
  - /user - cadastra um novo usuário no sistema, o corpo da requisição deve ser um JSON no seguinte formato:
 
        {
        'name': 'username',
        'email_address': 'example@example.com'
        }
  - /message - envia uma nova mensagem para algum usuário do sistema, o corpo da requisição deve ser um JSON no seguinte formato:

        {
          'sender_email': 'remetente@email.com',
          'recipient_email': 'destinatario@email.com',
          'subject': 'Encontro no parque',
          'body': 'Fui ao parque ontem, não te encontrei lá.'
        }
- DELETE
  - /message?message_id=2 - exclui uma das mensagens que já foram enviadas cujo id é igual ao id informado na requisição;
  - /user?user_id=3 - exclui um usuário do sistema cujo id é igual ao id informado na requisição;

## Como usar
Para usar o aplicativo, você precisa clonar o repositório do GitHub usando o seguinte comando:
```
git clone https://github.com/Mathwebb/messages-web-service.git
```

O aplicativo usa as seguintes bibliotecas, todas estão incluídas na biblioteca padrão do Python, portanto, não é necessário instalar nenhuma delas:
- http.server
- json
- sqlite3

Para poder executar o aplicativo, você precisa ter o Python na versão 3.10.6 ou superior, também é necessário usar o seguinte comando no diretório raiz do projeto para iniciar o servidor http:
- python3 src/server.py (Linux)
- python src/server.py (Windows)

Depois de iniciar o servidor, você pode continuar a usar o aplicativo abrindo seu navegador e acessando http://localhost:8000/login. Testei o aplicativo no Firefox e Opera GX, mas deve funcionar em qualquer outro navegador de sua preferência.
