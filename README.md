# Jamaica Stock Portfolio Manager

A local web application for managing and tracking your Jamaica Stock Exchange (JSE) portfolio. This application helps investors monitor their stock holdings by automatically fetching daily market data and calculating current portfolio values.

## Features

The application provides a comprehensive set of tools for stock portfolio management:

- Track your JSE stock holdings in a local database
- Automatic daily stock price updates through web scraping
- Calculate current market value of your portfolio
- View historical performance trends
- Manage multiple stock purchases and sales
- Generate portfolio reports and analytics

## Technology Stack

This project is built using modern web technologies:

- Frontend: React.js for a responsive and interactive user interface
- Backend: Python FastAPI for efficient API endpoints
- Database: SQLite for local data storage
- Docker: Containerization for easy setup and deployment

## Prerequisites

Before running the application, ensure you have the following installed:

- Docker and Docker Compose
- Git (for version control)

## Getting Started

1. Clone the repository:

   ```bash
   git clone [repository-url]
   cd stock-portfolio
   ```

2. Start the application using Docker Compose:

   ```bash
   # For development
   docker-compose -f docker-compose.dev.yml up

   # For production
   docker-compose up
   ```

3. Access the application:
   - Open your browser and navigate to `http://localhost:3000`
   - The API will be available at `http://localhost:8000`

## Project Structure

```
stock-portfolio/
├── frontend/                  # React application
├── backend/                   # Python FastAPI application
├── data/                     # Local data storage
├── docker/                   # Docker configuration
└── [configuration files]
```

Each directory contains its own README with specific documentation.

## Development

The project is set up for both development and production environments:

- Development mode includes hot-reloading for both frontend and backend
- Local database file is stored in `./data/portfolio.db`
- Development configuration uses `docker-compose.dev.yml`

## Local Data Storage

All data is stored locally:

- Database file location: `./data/portfolio.db`
- Backup files are created automatically in `./data/backups/`
- No external servers or cloud storage are used

## Security Notes

Since this application handles financial data:

- All data is stored locally on your machine
- No external connections except for stock price updates
- Regular database backups are recommended
- Keep your system and the application updated

## Troubleshooting

Common issues and solutions:

1. Database Connection Issues:

   - Ensure the data directory has proper permissions
   - Check if SQLite is properly installed in the container

2. Web Scraping Problems:
   - Verify your internet connection
   - Check if the stock website structure has changed
   - Review the scraping logs in `./backend/logs/`

## Contributing

To contribute to the project:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Include your chosen license information here]

## Contact

[Include contact information or links to issue reporting]
