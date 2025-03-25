# EventGearSauce
An example deployment of [Django](https://www.djangoproject.com/) and [React](https://react.dev/) for an event equipment rental company.

The development approach followed uses a Django-based server for the backend (ORM and API) and a ReactJS server for the frontend, to be able to use
the flexibility that React offers with components.

The [Django REST framework](https://www.django-rest-framework.org/) is used to create an API in the backend server project that the frontend server consumes to provide requested information from the SQLite3 database. The model currently only consists of two items (EquipmentStockItem and Quotation), and these two classes are linked using a many-to-many relationship, as quotations may use many equipment items from available stock, and many equipment items may appear on many quotations.

User registration and authentication is currently performed by using JSON Web Tokens (JWT), and only authenticated users may create quotations and add equipment stock items. This is achieved using the [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) library.

This website example is a work in progress.

Thanks to [William S. Vincent](https://github.com/wsvincent/) for his book series on Django development, and [TechWithTim](https://www.youtube.com/@TechWithTim) for the helpful videos on Django and React.
