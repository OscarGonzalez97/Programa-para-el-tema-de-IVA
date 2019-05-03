-- Table: public.iva10

-- DROP TABLE public.iva10;

CREATE TABLE public.iva10
(
  iva10_id serial NOT NULL,
  monto integer NOT NULL,
  mes character varying(255) NOT NULL,
  anho integer NOT NULL,
  concepto integer
  
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.iva10
  OWNER TO oscar;
COMMENT ON TABLE public.iva10
  IS 'Aqui se guardaran todas las facturas con su monto, concepto, mes y anho de un contribuyente';

-- Table: public.iva5

-- DROP TABLE public.iva5;

CREATE TABLE public.iva5
(
  iva5_id serial NOT NULL,
  monto integer NOT NULL,
  mes character varying(255) NOT NULL,
  anho integer NOT NULL,
  concepto integer
  
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.iva5
  OWNER TO oscar;
COMMENT ON TABLE public.iva5
  IS 'Aqui se guardaran todas las facturas con su monto, concepto, mes y anho de un contribuyente';

-- Table: public.iva5

-- DROP TABLE public.iva5;

CREATE TABLE public.exenta
(
  exenta_id serial NOT NULL,
  monto integer NOT NULL,
  mes character varying(255) NOT NULL,
  anho integer NOT NULL,
  concepto integer
  
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.exenta
  OWNER TO oscar;
COMMENT ON TABLE public.exenta
  IS 'Aqui se guardaran todas las facturas con su monto, concepto, mes y anho de un contribuyente';