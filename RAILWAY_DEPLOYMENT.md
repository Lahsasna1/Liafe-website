# Railway deployment

## Keep one persistent PostgreSQL database

1. In the Railway project, create a **single PostgreSQL** service if one does not already exist. Do not create one on each deployment.
2. Open the LIAFE web service, then **Variables** and add a reference variable named `DATABASE_URL`.
3. Set its value to `${{Postgres.DATABASE_URL}}`. Replace `Postgres` with the exact name of the existing PostgreSQL service if you renamed it.
4. Set these web-service variables:

   ```text
   DEBUG=False
   SECRET_KEY=<a long random secret>
   ALLOWED_HOSTS=ukliafe.com,www.ukliafe.com,${{RAILWAY_PUBLIC_DOMAIN}}
   CSRF_TRUSTED_ORIGINS=https://ukliafe.com,https://www.ukliafe.com,https://${{RAILWAY_PUBLIC_DOMAIN}}
   ```

5. Redeploy the web service. The pre-deploy step runs migrations only; it does not run either seed command, so your admin edits remain unchanged.

## Important

- `db.sqlite3` must only be used locally. Railway's app disk is rebuilt per deploy and is not a database.
- The PostgreSQL service's data persists independently of web-service deployments. Do not delete that service or use Railway's **New** database action after it contains live data.
- If the current live data is in a previous Railway PostgreSQL service, point `DATABASE_URL` at that service. Do not point it at a newly created one.
- This project now refuses to start with `DEBUG=False` and no `DATABASE_URL`, giving a useful deployment-log error instead of starting on a throwaway database.
