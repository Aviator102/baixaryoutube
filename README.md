# Downloader YouTube

Este projeto permite baixar vídeos e áudios do YouTube em diferentes resoluções usando Python.

<br/>

## Estrutura do Projeto

```css
downloaderYoutube/
├── main.py
├── venv/
├── video/
```

- **`main.py`**: O main contém a lógica para baixar vídeos e áudios do YouTube.
- **`venv/`**: Ambiente virtual Python, usado para isolar dependências do projeto.
- **`video/`**: Diretório onde os vídeos e áudios baixados serão armazenados.

<br/>

## Pré-requisitos

1. **Python 3.8 ou superior** instalado no sistema.  
   [Download do Python](https://www.python.org/).

2. **Visual Studio Code**.  
   [Download do VSCode](https://code.visualstudio.com/).

3. **Extensão Python Visual Studio Code**.   
   [Link da Extensão](https://code.visualstudio.com/docs/languages/python).

<br/>

## Configuração do Projeto

### 1. Crie o Ambiente Virtual
Abra o terminal na pasta raiz do projeto e execute o seguinte comando para criar o ambiente virtual:

```bash
python -m venv venv
```

### 2. Ative o Ambiente Virtual
- No Windows (CMD):

   ```bash
   venv\Scripts\activate.bat
   ```

- No Windows (PowerShell):

   ```bash
   venv\Scripts\Activate.ps1
   ```

- No macOS/Linux:

   ```bash
   source venv/bin/activate
   ```

### 3. Instale as Dependências
Com o ambiente virtual ativo, execute:

```bash
pip install pytubefix
```
### 4. Executando o Projeto
Certifique-se de que o ambiente virtual está ativo. Execute o main.py no terminal:

```bash
python main.py
```
O vídeo e o áudio baixados serão salvos no diretório **video/**.

### Problemas Comuns
- Erro ao Ativar Ambiente Virtual no PowerShell. Se você receber um erro ao ativar o ambiente virtual no PowerShell, execute:

   ```bash
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
- Erro ao Baixar Vídeos do YouTube. Se houver problemas com downloads, atualize o pacote pytubefix:

   ```bash
   pip install --upgrade pytubefix
   ```

<br/>

### Colaboradores

- [Carlos Longhi](https://github.com/CarlosLonghi)
- [Lucas Rissi](https://github.com/LRissi)
