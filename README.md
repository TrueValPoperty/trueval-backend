# TrueVal Backend

A clean Flask backend to support TrueVal's property valuation system with TrueVal ID integration.

## Endpoints

- `POST /log`: Accepts property data and logs it to Airtable, generating a unique `TrueVal ID`.

## Structure

- `app.py`: Main entry
- `routes/log.py`: `/log` route logic
- `utils/id_generator.py`: `generate_trueval_id()` function
- `airtable.py`: (You must configure Airtable credentials)

## Deployment

This project includes a `render.yaml` for easy deployment on [Render](https://render.com).

---

## 💬 Questions or Contributions?

Open an issue or reach out directly:

- 📧 William Tyler-Street: williamtylerstreet@gmail.com  
- 🏢 TrueVal Support: hello@trueval.co.uk
