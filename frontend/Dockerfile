# Build stage
FROM node:18-alpine as builder

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy source files
COPY . .

# Build app
RUN npm run build

# Production stage - serve with Node
FROM node:18-alpine

WORKDIR /app

# Install serve to run the built app
RUN npm install -g serve

# Copy built app from builder
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/package*.json ./

# Install production dependencies
RUN npm install

EXPOSE 5173

# Serve the app
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]
