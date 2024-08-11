# Stage 1: Build the Angular application
FROM node:18 as build

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application files
COPY . .

# Build the Angular application
RUN npm run build --prod

# Stage 2: Serve the application using nginx-unprivileged
FROM nginxinc/nginx-unprivileged:stable-alpine

# Copy the built Angular files from Stage 1
COPY --from=build /app/dist/counter-app-frontend /usr/share/nginx/html

# Copy custom Nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 8080 (default port for unprivileged Nginx)
EXPOSE 8080

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]