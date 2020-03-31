-- Archivo para creat tabla --
use lab_mysql;
CREATE TABLE IF NOT EXISTS `lab_mysql`.`Invoice` (
  `idInvoice` INT NOT NULL AUTO_INCREMENT,
  `date` DATE NOT NULL,
  `Staff ID` INT NOT NULL,
  `Customer ID` VARCHAR(45) NOT NULL,
  `VIN` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idInvoice`, `Customer ID`, `VIN`),
  UNIQUE INDEX `idInvoice_UNIQUE` (`idInvoice` ASC),
  INDEX `fk_Invoice_Salesperson1_idx` (`Staff ID` ASC),
  INDEX `fk_Invoice_Customer1_idx` (`Customer ID` ASC),
  INDEX `fk_Invoice_Car1_idx` (`VIN` ASC),
  CONSTRAINT `fk_Invoice_Salesperson1`
    FOREIGN KEY (`Staff ID`)
    REFERENCES `lab_mysql`.`Salesperson` (`Staff ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Invoice_Customer1`
    FOREIGN KEY (`Customer ID`)
    REFERENCES `lab_mysql`.`Customer` (`Customer ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Invoice_Car1`
    FOREIGN KEY (`VIN`)
    REFERENCES `lab_mysql`.`Car` (`VIN`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
--ENGINE = InnoDB;


