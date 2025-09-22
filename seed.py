from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing, Booking, Review
from faker import Faker
import random
from datetime import timedelta, date

fake = Faker()

class Command(BaseCommand):
    help = 'Seed the database with sample listings, bookings, and reviews'

    def handle(self, *args, **kwargs):
        self.stdout.write("Seeding database...")

        # Create users
        for _ in range(5):
            User.objects.get_or_create(
                username=fake.user_name(),
                email=fake.email(),
                password='pbkdf2_sha256$260000$dummy$hashedpassword'
            )

        users = list(User.objects.all())

        # Create listings
        for _ in range(10):
            Listing.objects.create(
                title=fake.sentence(nb_words=4),
                description=fake.paragraph(),
                location=fake.city(),
                price_per_night=random.randint(50, 500),
                host=random.choice(users)
            )

        listings = list(Listing.objects.all())

        # Create bookings
        for _ in range(15):
            listing = random.choice(listings)
            guest = random.choice(users)
            check_in = fake.date_between(start_date='-30d', end_date='today')
            check_out = check_in + timedelta(days=random.randint(1, 7))
            Booking.objects.create(
                listing=listing,
                guest=guest,
                check_in=check_in,
                check_out=check_out,
                total_price=(check_out - check_in).days * listing.price_per_night
            )

        bookings = list(Booking.objects.all())

        # Create reviews
        for booking in bookings:
            if random.choice([True, False]):
                Review.objects.create(
                    booking=booking,
                    rating=random.randint(1, 5),
                    comment=fake.sentence()
                )

        self.stdout.write(self.style.SUCCESS("Database seeding complete!"))