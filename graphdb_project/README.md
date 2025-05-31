# Django GraphDB Example

## Quickstart

1. Start GraphDB on Docker:
   ```
   docker run -d --name graphdb -p 7200:7200 --restart unless-stopped ontotext/graphdb:latest
   ```
2. Create a repository in GraphDB (e.g., `test`).

3. Edit `graphdata/utils.py` and set the repository name in the SPARQL endpoint URL.

4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Run Django migrations:
   ```
   python manage.py migrate
   ```

6. Start the Django development server:
   ```
   python manage.py runserver
   ```

7. Open http://localhost:8000/ in your browser.

---

*For questions, ask Avgoustinos!*
