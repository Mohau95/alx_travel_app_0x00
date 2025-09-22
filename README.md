# alx_travel_app_0x00

## Milestone 2 - Creating Models, Serializers, and Seeders

This project implements core backend components for a travel booking application.

### Features Implemented:
- **Models:** Listing, Booking, Review with proper relationships.
- **Serializers:** For Listing and Booking models.
- **Seeder:** Management command to populate the database with realistic sample data.

### How to Run Seeder:
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py seed
```

### Dependencies:
- Django
- Django REST Framework
- Faker