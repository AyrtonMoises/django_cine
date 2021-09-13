FROM nginx:1.21-alpine
LABEL Ayrton Sousa
COPY /docker/config/ /etc/nginx/
EXPOSE 80 443
ENTRYPOINT ["nginx"]
# Parametros extras para o entrypoint
CMD ["-g", "daemon off;"]